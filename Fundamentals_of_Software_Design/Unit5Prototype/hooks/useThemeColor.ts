import { Colors } from '@/constants/Colors';
import { useColorScheme } from './useColorSchemeContext';

export function useThemeColor(
  props: { light?: string; dark?: string },
  colorName: keyof typeof Colors.light & keyof typeof Colors.dark
) {
  const { colorScheme } = useColorScheme();
  const colorFromProps = props[colorScheme];

  if (colorFromProps) {
    return colorFromProps;
  }
  return Colors[colorScheme][colorName];
}