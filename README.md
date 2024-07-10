<h1>
    <a href="https://www.python.org">
     <img align="center" width="40px" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></a>
    <span>EmailAutomation</span>
</h1>

> [!NOTE]   
> This repository contains Python projects for automating emails using libraries.

## Resources 
<table>
  <thead>
    <tr align="left">
      <th>Name</th>
      <th>Version</th>
    </tr>
  </thead>
  <tbody align="left">
    <tr>
      <td>Python</td>
      <td>3.12.14</td>
    </tr>
    <tr>
      <td>imap_tools</td>
      <td>1.6.0</td>
    </tr>
    <tr>
      <td>smtplib</td>
      <td>native library</td>
    </tr>
  </tbody>
</table>

## Steps to reproduce
1. Install Python on your computer from the [`official website`](https://www.python.org) or use an online compiler like [`Google Colab`](https://colab.research.google.com);
2. Configure your Gmail account to allow access for less secure apps:
   - Go to Google Account Settings;
   - Click on "Security" in the left-hand sidebar;
   - Scroll down to the "Less secure app access" section;
   - Click on "Turn on access" or a similar option to enable access for less secure apps;
3. Clone this repository:
```bash
git clone https://github.com/Mileny-Nogueira/EmailAutomation
```
4. Execute the desired file using the following command:
```bash
py sendEmail.py
```
> [!IMPORTANT]   
> If your Gmail account has 2FA enabled, this script will not work.
