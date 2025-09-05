<h1 align="center">Urban Grocers Automation – Sprint 7 Commit</h1>

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:640/format:webp/1*xNQKHj5vR7w9AcY_bDKYYw.gif" alt="Project Logo">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-IN%20DEVELOPMENT-yellow" alt="Status">
  <img src="https://img.shields.io/badge/PYTEST-Passing-brightgreen" alt="Pytest Badge">
  <img src="https://img.shields.io/badge/Coverage-85%25-blue" alt="Coverage Badge">
  <img src="https://img.shields.io/github/stars/yourusername?style=social" alt="GitHub Stars">
</p>

---

## 📝 Project Description
This repository contains an **automated test suite** for validating the `Kit Name` functionality of an API.  
The tests were designed with a **QA Engineering approach**, ensuring that both positive and negative scenarios are covered to check API robustness and compliance with expected business rules.

The main objective is to validate:
- Kit creation with valid names.
- API responses when invalid or edge-case data is provided.
- Error handling when mandatory parameters are missing.

---

## 📑 Documentation
- API documentation source: [apiDoc](https://apidocjs.com/)  
- Test cases were designed based on the provided API specifications and QA best practices.

---

## 🚧 Project Status
<h4 align="center">
🚧 Under Development 🚧
</h4>

> Some negative tests currently fail due to backend validation gaps (e.g., empty names or numeric input are accepted instead of returning 400).  

---
 🎬 
<p align="center">
  <img src="https://i.pinimg.com/originals/79/9e/0d/799e0d7779f6ea6c3a89885ff60c55af.gif" alt="Test Execution GIF">
</p>

---

## ⚙️ Features & Tests
The test suite covers the following scenarios:

- ✅ Create kit with **1 character name** → `201`
- ✅ Create kit with **511 characters name** → `201`
- ❌ Attempt to create kit with **empty name** → Expected `400`
- ❌ Attempt to create kit with **512 characters name** → Expected `400`
- ✅ Create kit with **special characters** → `201`
- ✅ Create kit with **leading/trailing spaces** → `201`
- ✅ Create kit with **numeric string name** → `201`
- ❌ Attempt to create kit with **empty request body** → Expected `400`
- ❌ Attempt to create kit with **integer name** → Expected `400`

> ℹ️ Some tests may reveal inconsistencies between expected and actual behavior.  
> This is intentional, as it demonstrates how QA detects **bugs or missing validations** in the backend.

---

## 🛠️ Technologies & Techniques
- **Python 3.10+**
- **Pytest** for test execution
- **Requests** library for API calls
- **apiDoc** for API documenta

---

## Conclusion
This repository demonstrates QA skills in API automation testing, covering both positive and negative scenarios. It's a solid example of professional test design, assertion handling, and documentation for GitHub portfolios.

Contributions to improve backend validation coverage or add more test cases are welcome!

---

## To run the tests:
- Clone the repository to your local environment using SSH. Replace “username” with your GitHub username:
  ```sh
  git clone git@github.com:username/qa-project-Urban-Grocers-app-es.git
  ```
- If you don’t have them installed, install pytest and requests packages to run the tests:
  ```sh
  pip install requests pytest
  ```
- Run all tests with pytest:
  ```sh
   pytest
    ```

