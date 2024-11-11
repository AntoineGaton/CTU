import { Stack } from 'expo-router';
import { ColorSchemeProvider } from '@/hooks/useColorSchemeContext';

export default function RootLayout() {
  return (
    <ColorSchemeProvider>
      <Stack screenOptions={{ headerShown: false }}>
        <Stack.Screen name="(tabs)" />
      </Stack>
    </ColorSchemeProvider>
  );
}
