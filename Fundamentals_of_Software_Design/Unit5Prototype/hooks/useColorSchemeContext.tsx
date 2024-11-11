import { createContext, useContext, useState } from 'react';

// Define the type for our color scheme context
type ColorSchemeContextType = {
  colorScheme: 'light' | 'dark';
  toggleColorScheme: () => void;
};

// Create context with undefined default value
const ColorSchemeContext = createContext<ColorSchemeContextType | undefined>(undefined);

// Provider component that wraps our app
export function ColorSchemeProvider({ children }: { children: React.ReactNode }) {
  // State to track current color scheme
  const [colorScheme, setColorScheme] = useState<'light' | 'dark'>('dark');

  // Function to toggle between light and dark mode
  const toggleColorScheme = () => {
    setColorScheme((prev) => (prev === 'light' ? 'dark' : 'light'));
  };

  return (
    <ColorSchemeContext.Provider value={{ colorScheme, toggleColorScheme }}>
      {children}
    </ColorSchemeContext.Provider>
  );
}

// Custom hook to use the color scheme context
export function useColorScheme() {
  const context = useContext(ColorSchemeContext);
  if (!context) {
    throw new Error('useColorScheme must be used within a ColorSchemeProvider');
  }
  return context;
}