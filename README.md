# Chatbot

## Description:
This project aims to create a chatbot capable of answering user queries while also integrating a conversational form to collect user information such as Name, Email, Phone Number, and Address.

![image](https://github.com/HackerajOfficial/ChatBot/assets/46445015/acba7205-ca02-49fd-b93c-f337f534949f)

## Technologies Used:
- **Chatterbot:** Chatterbot is utilized for building the conversational AI, providing the chatbot with the capability to understand and respond to user queries.
- **spaCy:** spaCy is employed for natural language processing tasks such as tokenization, entity recognition, and text classification, enhancing the chatbot's understanding of user inputs.
- **Django:** Django framework for handling language processing tasks efficiently, enabling seamless integration with Chatterbot and spaCy.

## Features

- **Document Query:** The chatbot is trained to understand and respond to user queries based on the information provided in documents. It employs machine learning algorithms to comprehend the context of the queries and provide relevant responses.
- **Conversational Form:** When prompted by the user to call them, the chatbot initiates a conversation to collect essential user information, including Name, Email, Phone Number, and Address. The conversational form guides users through the information collection process, ensuring a smooth and engaging user experience.

## Usage:
1. Clone the repository to your local machine.
     ```
      git clone https://github.com/HackerajOfficial/ChatBot.git
     ```
2. Active environment
     ```
       venv\Scripts\activate
     ```
3. Install the necessary dependencies
    ```
      pip install -r requirements.txt
    ```
4. Start the Django development server:
    ```
      python manage.py runserver
    ```

5. Open your web browser and navigate to `http://localhost:8000`

6. Train ChatBot through Upload .txt Document  `http://localhost:8000/train` 

## Contributing
Contributions to enhance the functionality and performance of the chatbot are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request outlining the modifications.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code in accordance with the terms of the license.
## Contact:
For any inquiries or feedback regarding the project, please contact [RaazKapoorKuswaha](https://www.facebook.com/HackerajOfficial/) at hackeraj.np@gmail.com.
