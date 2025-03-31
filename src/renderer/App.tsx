// src/renderer/src/App.tsx
import React, { useState } from 'react';
import { textToMorse, morseToText } from '../main/morse'; // Import các hàm từ file utils
import './App.css'; // Import file CSS (sẽ tạo ở bước sau)

function App(): JSX.Element {
  const [inputText, setInputText] = useState<string>('');
  const [outputText, setOutputText] = useState<string>('');
  const [mode, setMode] = useState<'encode' | 'decode'>('encode'); // Lưu trữ chế độ hiện tại

  const handleInputChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInputText(event.target.value);
    // Tự động xóa kết quả khi input thay đổi
    setOutputText('');
  };

  const handleEncode = () => {
    setMode('encode');
    setOutputText(textToMorse(inputText));
  };

  const handleDecode = () => {
    setMode('decode');
    // Cần chuẩn hóa input Morse một chút (loại bỏ khoảng trắng thừa)
    const cleanedInput = inputText.trim().replace(/ +/g, ' ');
    setOutputText(morseToText(cleanedInput));
  };

  return (
    <div className="container">
      <h1>Morse Code Translator</h1>

      <div className="input-section">
        <label htmlFor="morse-input">Nhập văn bản hoặc mã Morse:</label>
        <textarea
          id="morse-input"
          value={inputText}
          onChange={handleInputChange}
          rows={5}
          placeholder="Nhập ở đây..."
        />
      </div>

      <div className="button-section">
        <button onClick={handleEncode}>Mã hóa sang Morse</button>
        <button onClick={handleDecode}>Giải mã từ Morse</button>
      </div>

      <div className="output-section">
        <label htmlFor="morse-output">Kết quả ({mode === 'encode' ? 'Morse' : 'Văn bản'}):</label>
        <textarea
          id="morse-output"
          value={outputText}
          readOnly // Kết quả chỉ để đọc
          rows={5}
          placeholder="Kết quả sẽ hiển thị ở đây..."
          className={mode === 'encode' ? 'morse-output' : 'text-output'}
        />
      </div>
    </div>
  );
}

export default App;
