# Guide in Poland

**Guide in Poland** is a terminal-based web application designed to provide valuable resources and services for individuals living in or moving to Poland. Unlike traditional web applications that run in a browser, this application is implemented in Python and runs directly in the terminal.

---

## Features

### 📝 News Page
Stay informed with the latest news and updates from Poland.

### 📚 Study Resources
Explore opportunities for education in Poland, including:
- Universities
- Courses
- Mentoring programs

### 💖 Donate
Support us in maintaining the platform with up-to-date resources and services. Your donations ensure the sustainability and quality of our application.

### 🧑🏻‍💻 Job Search
Find your next opportunity with our job board:
- Search for part-time, full-time, permanent, or contract-based jobs.
- Access a curated list of recommended job boards.

### 👨🏻‍⚖️ Legalisation Services
Resolve your legalisation issues with the help of our experienced lawyers and consultants. We are committed to helping you stay compliant with Polish regulations.

### ❓ FAQ
Visit our Frequently Asked Questions section to find answers to common queries. If your question is not listed, feel free to contact our support team for assistance.

### ⁉️ Report an Issue
Encountered an issue or an untrusted source? Report it to us, and we will address it promptly to ensure reliable and trustworthy resources for our users.

### 🎉 Social Media
Follow us on social media to stay updated on the latest events and announcements.

---

## Setup

### Prerequisites
Ensure Python 3.x is installed on your system.

### Installation Steps

#### 1. Clone the Repository
```
git clone https://github.com/daniiar-pro/guide_in_pl.git
```
#### 2. Install Dependencies (Packages)
```
 pip install -r requirements.txt
```
3. Configure API Keys Sign up for free API keys from : [news API](https://newsdata.io/documentation)
4. Create `.env` file in the root folder and store your `NEW_API_KEY=your_api_key`

## Usage
`python main.py`

- Above command runs the app, and follow the instructions that pops up when app has started

## Data Storage
All data is stored in  CSV, PDF format under the `info/` directory

## Future Enhancements
- Frontend Implementation: of the current application, for more Visual and better user experience
- User Authentication: Allow users sign up to keep them updated with latest events

![figma_design](https://github.com/user-attachments/assets/fa762052-fb57-4816-8a8b-9fb30ac8ef9e)






