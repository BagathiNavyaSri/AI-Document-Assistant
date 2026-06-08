# AI Document Assistant

An AI-powered document assistant that enables OCR extraction, semantic search, hybrid retrieval, and context-aware question answering across uploaded documents.

## Features

* OCR-based document extraction
* Hybrid Search (Semantic + Keyword Retrieval)
* Retrieval-Augmented Generation (RAG)
* Multi-file upload support
* Chat history management
* Source citations
* Confidence scoring
* Active file filtering
* User authentication and authorization
* Persistent cloud database storage

## Tech Stack

### Backend

* FastAPI
* Python
* SQLAlchemy

### Database

* PostgreSQL

### AI & Search

* Gemini 2.5 Flash
* FAISS
* Sentence Transformers

### Document Processing

* PyMuPDF
* PyPDF2
* Tesseract OCR
* OpenCV

### Frontend

* HTML
* CSS
* JavaScript

## Architecture

* Document Upload & Processing
* OCR & Text Extraction
* Chunking & Embedding Generation
* FAISS Vector Search
* Hybrid Retrieval
* Gemini-powered Answer Generation
* Source Citation & Confidence Scoring
* Chat History Persistence using PostgreSQL
