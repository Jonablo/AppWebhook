
# AppWebhook

## Description

AppWebhook is a simple example of how to create and test webhooks using Python and Flask. Webhooks allow applications to respond to events in real-time, and this project demonstrates how to set them up and handle them effectively.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

Follow these steps to set up the development environment:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jonablo/AppWebhook.git
   cd AppWebhook
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the receiver server**:
   ```bash
   python ServerReceiver.py
   ```

2. **Start the sender server**:
   In a new terminal, make sure the virtual environment is activated and run:
   ```bash
   python ServerSender.py
   ```

3. **Test the webhook**:
   The sender server will send a POST request to the receiver server, which will handle the webhook and display the received information in the console.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.