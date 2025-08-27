from django import template

register = template.Library()


@register.filter(name="check_slash")
def check_slash(value: str):
    """
    Check if a string contains newline characters.
    
    This Django template filter determines whether the input string contains
    any newline characters (\n). It returns True if newlines are present,
    False otherwise.
    
    Args:
        value (str): The input string to be checked for newline characters.
    
    Returns:
        bool: True if the string contains one or more \n characters,
              False if no newline characters are found.
    
    Example:
        Input: "Hello\nWorld"
        Output: True
        
        Input: "Hello World"
        Output: False
        
        Template usage:
        {% load custom_filters %}
        {% if note|check_slash %}
            <p>This note contains line breaks</p>
        {% endif %}
    
    Note:
        This filter is commonly used in templates to conditionally render
        different HTML structures based on whether text content spans
        multiple lines. Useful for applying different styling or formatting
        to single-line vs multi-line text content.
    """
    if "\n" in value:
        return True
    return False


@register.filter(name="list_converter")
def list_converter(value: str):
    """
    Convert a multiline string into a list by splitting on carriage returns and cleaning newlines.
    
    This Django template filter takes a string containing carriage return characters (\r)
    and optionally newline characters (\n), then converts it into a list of clean strings.
    Each carriage return acts as a delimiter for list items, and any newline characters
    within items are stripped out.
    
    Args:
        value (str): The input string to be converted. Expected to contain \r characters
                    as line separators and potentially \n characters to be removed.
    
    Returns:
        list[str]: A list of strings where:
                  - Each element corresponds to text between \r characters
                  - All \n characters have been removed from individual elements
                  - Empty strings may be included if there are consecutive \r characters
    
    Example:
        Input: "Hello\nWorld\rSecond Line\rThird\nLine"
        Output: ['HelloWorld', 'Second Line', 'ThirdLine']
        
        Template usage:
        {% load custom_filters %}
        {{ my_string|list_converter }}
    
    Note:
        This filter is particularly useful for processing textarea input that may contain
        mixed line ending formats (Windows-style \r\n, Unix-style \n, or Mac-style \r).
    """
    split_list = value.split("\r")
    final = []
    new_word = []
    for item in split_list:
        if "\n" in item:
            for letter in item:
                if letter != "\n":
                    new_word.append(letter)

            final.append("".join(new_word))
        else:
            final.append(item)
    return final
