# Meeting Reminder Bot 👾

A simple Discord bot that helps you set reminders for upcoming meetings and sends you notifications. You can use the bot to schedule meetings and specify the time and date for each meeting.

## 🌟 Features

- Set Meeting Reminders: Use the bot to set reminders for your meetings. Specify the date and optional time for the meeting.
- Receive Notifications: The bot will send you a notification at the specified time and date to remind you of your meeting.

## 🌟 Commands
Set a reminder for a meeting on a specific date and optional time:
> !spotkanie _DD-MM-YYYY_ _HH-MM_ <br>

or <br>
> !spotkanie _DD-MM-YYYY_

Set a default time for the reminder:
> !czas _HH-MM_

## 🌟 Setup

To use the bot, you need a Discord token and the ID of the channel you want the bot to operate in.

- Token: Obtain your Discord bot token from the Discord Developer Portal.
- Channel ID: Copy the ID of the channel where you want the bot to send reminders.

## 🌟 How to Use

1. Clone the repository to your local machine.<br>
  `git clone https://github.com/buennoo/MeetingReminder-bot.git`
2. Head to [Discord Developer Portal](https://discord.com/developers/applications), create an app and generate the **token** in Bot section.

3. [Set up](#-setup) the bot by providing your Discord token and channel ID (that you have previously copied) from your discord server in the main.py file.
  
4. Run the bot using these commands in terminal:<br>
   `cd <<here provide the path to the cloned folder>>`<br>
   `python main.py`
