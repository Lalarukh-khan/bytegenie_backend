### Getting Started

<p align="center">
    <a href="https://www.loom.com/share/49ed118f275040a5b51c6bb375e3668d?sid=31f726fc-a076-4d6c-98f5-257f8f5aed99">Project Demo Video</a>
    <br /><br />
</p>

This is a document related various task performing NLP project. Client-side code is in the client folder, server code is in this folder. If you want to install the entire system for development purposes install the python this way:

Virtualenv generation:

```
python3 -m venv venv
```
```
source venv/bin/activate
```

Install python packages:
```
pip3 install Flask
```
```
pip3 install transformers
```
```
pip3 install torch torchvision
```

How to start backend server:

```
python3 server.py
```

Browser route for project backend running:

```
http://localhost:5000
( or ) http://localhost:5000/testing/
```


that is all.

# A Brief Description of Backend Project

### Main steps and motivation for any data engineering/processing on the raw data before making it available to the API

- Ran the plain server on testing route
- Through transformer and pipeline tested Text-Generation modal
- Used various modals of HuggingFace 

### The main functionalities of the API

There are 2 APIs developed on backend server: 
1. /Answer (Developed for Question-Answer HuggingFace Modal)
2. /Summary (Developed for Summarization HuggingFace Modal)


### the key challenges you faced in solving the problem;

There were not major hurdles on the way of backend development, however on some core sections took time in deployment

- Tokenizer and modal testing:
	Tested different modals, all modal were having specific pattern to receive on server, so it took time in going through whole documentation and workflow

- Indentation and Functions format:
	Wrote clean code, faced indentation problems in If-Else functions, tried to cover proper format and manageable format.

### how would you improve the backend, if you had more time to work on it?

I definitely got huge time till 1st of Jan and till that time I know I could add more things in the backend. I tried to cover tasks with less code. Yes, I wanted to develop some more backend functionalities using other tools other than Huggingfaces, I found Huggingface most interested but LLM APIs or Sentence-Transformers Library are also best to use 😄