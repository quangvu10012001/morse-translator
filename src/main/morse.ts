// src/renderer/src/utils/morse.ts
export const MORSE_CODE_DICT: { [key: string]: string } = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
  'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
  'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
  '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/' // Dùng '/' cho khoảng trắng giữa các từ
};

// Tạo dictionary đảo ngược để giải mã
export const MORSE_CODE_DICT_REVERSE: { [key: string]: string } = Object.entries(
  MORSE_CODE_DICT
).reduce((acc, [key, value]) => {
  acc[value] = key;
  return acc;
}, {} as { [key: string]: string });

export function textToMorse(text: string): string {
  return text
      .toUpperCase()
      .split('')
      .map(char => MORSE_CODE_DICT[char] || '') // Bỏ qua ký tự không có trong dict
      .join(' ') // Khoảng cách giữa các ký tự Morse
      .replace(/ +\/ +/g, ' / '); // Đảm bảo khoảng cách đúng quanh dấu / cho từ
}

export function morseToText(morse: string): string {
 // Tách các từ Morse bằng ' / ', sau đó tách các chữ cái Morse bằng ' '
 return morse
      .split(' / ') // Tách thành các từ
      .map(word =>
          word
              .split(' ') // Tách thành các mã Morse cho từng ký tự
              .map(code => MORSE_CODE_DICT_REVERSE[code] || '') // Chuyển mã thành ký tự, bỏ qua mã không hợp lệ
              .join('') // Ghép các ký tự thành từ
      )
      .join(' '); // Ghép các từ lại, thêm khoảng trắng giữa các từ
}
