
# 📝 Notes Application

A simple and elegant Django-based notes application that allows users to create, manage, and organize their notes with an intuitive web interface.

## ✨ Features

- **Simple Note Creation**: Add notes through a clean, user-friendly interface
- **Smart Note Formatting**: 
  - Regular notes display as styled cards
  - Slash-separated notes (`/`) are automatically split into organized lists
- **Real-time Updates**: Notes appear instantly after submission
- **Responsive Design**: Bootstrap-powered UI that works on all devices
- **Empty State Handling**: Helpful messaging when no notes exist
- **Note Counter**: Badge showing total number of notes

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd notes-app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m virtualenv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## 🎯 Usage

### Adding a Note
1. Navigate to the main page
2. Enter your note in the text area
3. Click "Add Note" to save
4. Your note appears instantly below

### Note Formatting
- **Regular Notes**: Display as styled cards with sticky note icons
- **Slash-Separated Notes**: Notes containing `/` are automatically split into multiple bullet-pointed items
- **Empty State**: Helpful message and icon when no notes exist

## 🏗️ Project Structure
