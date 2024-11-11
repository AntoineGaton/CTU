# Product Search App 👋

A modern React Native application built with Expo, featuring real-time product search functionality and theme customization.

## Features

- **Real-time Product Search**: Instantly filter products as you type
- **Dark/Light Mode**: Toggle between dark and light themes with a single tap
- **Interactive UI Elements**: 
  - Animated welcome wave
  - Image enlargement on tap
  - Smooth transitions
- **Responsive Design**: Works seamlessly across different screen sizes
- **Cross-Platform**: Compatible with both iOS and Android

## Getting Started

1. Install dependencies
   ```bash
   npm install
   ```

2. Start the development server
   ```bash
   npx expo start
   ```

3. Run on your preferred platform:
   - Press `i` for iOS simulator
   - Press `a` for Android emulator
   - Scan QR code with Expo Go app for physical devices

## App Structure

- **/app**: Main application code using file-based routing
  - **(tabs)**: Tab-based navigation screens
    - `index.tsx`: Home screen with app information
    - `search.tsx`: Product search functionality
- **/components**: Reusable UI components
- **/constants**: App-wide constants including theme colors
- **/hooks**: Custom React hooks for state management

## Theme Support

The app comes with a built-in theme system:
- Starts in Dark mode by default
- Toggle between themes using the sun/moon icon in the header
- Consistent theming across all components
- Smooth theme transitions

## Development

Created by Antoine Gaton using:
- React Native
- Expo Router
- React Native Reanimated
- TypeScript

## Learn More

To understand the codebase better:
- [Expo Documentation](https://docs.expo.dev/)
- [React Native](https://reactnative.dev/)
- [Expo Router](https://docs.expo.dev/router/introduction/)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
