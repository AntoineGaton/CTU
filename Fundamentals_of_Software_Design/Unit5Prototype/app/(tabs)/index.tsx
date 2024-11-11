import { Image, StyleSheet, ScrollView } from 'react-native';

import { HelloWave } from '@/components/HelloWave';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';

export default function HomeScreen() {
  return (
    <ThemedView style={styles.container}>
      <ThemedView style={styles.headerContainer}>
        <Image
          source={require('@/assets/images/partial-react-logo.png')}
          style={styles.headerImage}
        />
      </ThemedView>
      
      <ScrollView style={styles.scrollContainer} contentContainerStyle={styles.scrollContent}>
        <ThemedView style={styles.titleContainer}>
          <ThemedView style={styles.titleWrapper}>
            <ThemedText type="title">Product Search App</ThemedText>
            <HelloWave />
          </ThemedView>
        </ThemedView>
        
        <ThemedView style={styles.stepContainer}>
          <ThemedText type="subtitle" style={styles.subtitle}>About This App</ThemedText>
          <ThemedText>
            This mobile application created by <ThemedText style={styles.highlight}>Antoine Gaton</ThemedText> showcases a modern{' '}
            <ThemedText style={styles.highlight}>product search</ThemedText> implementation with 
            real-time filtering and an intuitive user interface. Built with{' '}
            <ThemedText style={styles.highlight}>React Native</ThemedText> and{' '}
            <ThemedText style={styles.highlight}>Expo</ThemedText>, it demonstrates efficient state 
            management and responsive design principles.
          </ThemedText>
        </ThemedView>
        
        <ThemedView style={styles.stepContainer}>
          <ThemedText type="subtitle" style={styles.subtitle}>Key Features</ThemedText>
          <ThemedText>
            • <ThemedText style={styles.highlight}>Instant search</ThemedText> with multi-field filtering{'\n'}
            • <ThemedText style={styles.highlight}>Interactive product cards</ThemedText> with image preview{'\n'}
            • <ThemedText style={styles.highlight}>Smooth animations</ThemedText> and transitions{'\n'}
            • Clean, modern user interface{'\n'}
            • Cross-platform compatibility
          </ThemedText>
        </ThemedView>
        
        <ThemedView style={styles.stepContainer}>
          <ThemedText type="subtitle" style={styles.subtitle}>How to Use</ThemedText>
          <ThemedText>
            Navigate to the <ThemedText style={styles.highlight}>Search</ThemedText> tab to explore products. 
            The search function filters through <ThemedText style={styles.highlight}>product names</ThemedText>,{' '}
            <ThemedText style={styles.highlight}>categories</ThemedText>, and{' '}
            <ThemedText style={styles.highlight}>prices</ThemedText> in real-time. 
            Tap on any product image to view an enlarged version. The interface is designed 
            to be intuitive and user-friendly, providing a seamless shopping experience.
          </ThemedText>
        </ThemedView>
      </ScrollView>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  headerContainer: {
    height: 200,
    width: '100%',
    position: 'absolute',
    top: 0,
    backgroundColor: '#A1CEDC',
  },
  headerImage: {
    height: 225,
    width: 290,
    resizeMode: 'contain',
  },
  scrollContainer: {
    flex: 1,
    marginTop: 200,
  },
  scrollContent: {
    padding: 16,
  },
  titleContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    marginBottom: 16,
  },
  titleWrapper: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  titleColor: {
    color: '#A5CEDC',
  },
  stepContainer: {
    gap: 12,
    marginBottom: 24,
    padding: 16,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ccc',
  },
  subtitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#A5CEDC',
  },
  italicColor: {
    color: '#A5CEDC',
  },
  highlight: {
    color: '#A5CEDC',
    fontStyle: 'italic',
  },
});
