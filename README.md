# 📡 Morse Code Translator App

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ## 📂 Project Structure

```plaintext
📁 morse-translator
├── 📁 electron
│   ├── 📄 preload.ts       # Preload script for renderer
├── 📁 src
│   ├── 📁 renderer
│   │   ├── 📄 App.tsx      # Main React component
│   ├── 📁 main
│   ├── ├── 📄 main.ts      # Electron main process
│   │   ├── 📄 morse.ts     # Morse code logic
├── 📄 electron.vite.config.ts # Electron Vite configuration
![License](https://img.shields.io/badge/license-MIT-blue) 
![Version](https://img.shields.io/badge/version-v1.0.0-orange) 
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)

## 💬 Introduction

The **Morse Code Translator App** is a desktop application that allows users to seamlessly convert text to Morse code and vice versa. Whether you're learning Morse code or need a quick and reliable tool for encoding/decoding, this app has you covered! Built with modern web technologies like React, Electron, and TypeScript, it offers a simple and intuitive interface for all users. ↔️

---

## 📸 Visuals

[Screenshot Placeholder: Add a nice screenshot/GIF of the app interface here!]

---

## 🌟 Features

- ✅ Encode standard text to International Morse Code.
- ✅ Decode International Morse Code (dots, dashes, spaces, slashes) back to text.
- ✅ Simple and intuitive user interface.
- ✅ Cross-platform compatibility (thanks to Electron).
- ✅ Built with modern web technologies.

---

## 🛠️ Tech Stack

- ⚛️ **React**: Frontend framework for building the user interface.
- ⚡ **Electron**: Enables cross-platform desktop application development.
- 🛠️ **TypeScript**: Ensures type safety and better developer experience.
- 🛠️ **Vite**: Lightning-fast build tool for modern web projects.
- 💻 **Node.js**: Backend runtime for Electron.
- 🎨 **CSS**: For styling the application.

---

## 📂 Project Structure

```plaintext
📁 morse-translator
├── 📁 electron
│   ├── 📄 main.ts          # Electron main process
│   ├── 📄 preload.ts       # Preload script for renderer
├── 📁 src
│   ├── 📁 renderer
│   │   ├── 📄 App.tsx      # Main React component
│   │   ├── 📁 utils
│   │   │   ├── 📄 morse.ts # Morse code logic
├── 📄 electron.vite.config.ts # Electron Vite configuration
````

## 💻 Installation

Follow these steps to set up the project locally:

Clone the repository:

```bash
git clone https://github.com/your-username/morse-translator.git
```

Navigate into the project directory:

```bash
cd morse-translator
```

Install dependencies:

```bash
npm install
```

Or, if you prefer Yarn:

```bash
yarn install
```

## 🚀 Usage / Running the App

To run the application in development mode:

```bash
npm run dev
```

Or, if using Yarn:

```bash
yarn dev
```

## ⚙️ Building for Production

To build the application for distribution:

```bash
npm run build
```

Or, if using Yarn:

```bash
yarn build
```

The build output will be available in the `dist` directory.

## 📜 Morse Code Format

The app uses the following format for Morse code input:

- Dot: `.`
- Dash: `-`
- Letter separator: (space)
- Word separator: `/` (slash)

Example:

```
HELLO WORLD → .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please check out the Contributing Guidelines (placeholder).

## ✨ Acknowledgements

Thanks to the creators of React, Electron, and Vite for their amazing tools.
Special thanks to the open-source community for inspiration and support. ❤️
