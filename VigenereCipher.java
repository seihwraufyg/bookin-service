import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class VigenereCipher {

    /**
     * Метод для шифрования текста
     */
    public static String encrypt(String plaintext, String key) {
        StringBuilder ciphertext = new StringBuilder();
        key = key.toUpperCase(); // Приводим ключ к верхнему регистру для удобства расчетов
        int keyIndex = 0;
        int keyLength = key.length();

        for (int i = 0; i < plaintext.length(); i++) {
            char currentChar = plaintext.charAt(i);

            // Проверяем, является ли символ буквой
            if (Character.isLetter(currentChar)) {
                // Определяем сдвиг: 'A' -> 0, 'B' -> 1, ...
                int shift = key.charAt(keyIndex % keyLength) - 'A';

                // Определяем базовый код (для заглавных 'A' = 65, для строчных 'a' = 97)
                char base = Character.isUpperCase(currentChar) ? 'A' : 'a';

                // Шифруем символ: (текущий код - база + сдвиг) % 26 + база
                char encryptedChar = (char) ((currentChar - base + shift) % 26 + base);

                ciphertext.append(encryptedChar);
                keyIndex++; // Переходим к следующей букве ключа только если символ был буквой
            } else {
                // Если это пробел или знак препинания, оставляем как есть и НЕ сдвигаем ключ
                ciphertext.append(currentChar);
            }
        }
        return ciphertext.toString();
    }

    /**
     * Метод для дешифрования текста
     */
    public static String decrypt(String ciphertext, String key) {
        StringBuilder plaintext = new StringBuilder();
        key = key.toUpperCase();
        int keyIndex = 0;
        int keyLength = key.length();

        for (int i = 0; i < ciphertext.length(); i++) {
            char currentChar = ciphertext.charAt(i);

            if (Character.isLetter(currentChar)) {
                int shift = key.charAt(keyIndex % keyLength) - 'A';
                char base = Character.isUpperCase(currentChar) ? 'A' : 'a';

                char decryptedChar = (char) ((currentChar - base - shift + 26) % 26 + base);

                plaintext.append(decryptedChar);
                keyIndex++;
            } else {
                plaintext.append(currentChar);
            }
        }
        return plaintext.toString();
    }

public static void main(String[] args) throws IOException {
String key = "KEY"; 

        String originalText = new String(Files.readAllBytes(Paths.get("input.txt")));
        originalText = originalText.trim(); 

        System.out.println("Original text from file: " + originalText);
        System.out.println("Key: " + key);

        String encryptedText = encrypt(originalText, key);
        System.out.println("Encrypted text: " + encryptedText);

        Files.write(Paths.get("output.txt"), encryptedText.getBytes());
        System.out.println("SUCCESS: Encrypted text saved to output.txt");

        String decryptedText = decrypt(encryptedText, key);
        System.out.println("Decrypted text: " + decryptedText);
    }
}