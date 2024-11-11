import { useState } from 'react';
import { StyleSheet, TextInput, FlatList, Image, Modal, TouchableOpacity, Dimensions } from 'react-native';
import { ThemedView } from '@/components/ThemedView';
import { ThemedText } from '@/components/ThemedText';
import { PRODUCTS, Product } from '@/data/productData';
import { Ionicons } from '@expo/vector-icons';

export default function SearchScreen() {
  const [searchQuery, setSearchQuery] = useState('');
  const [results, setResults] = useState(PRODUCTS);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);

  const handleSearch = (text: string) => {
    setSearchQuery(text);
    if (text.trim() === '') {
      setResults(PRODUCTS);
      return;
    }
    
    const searchTerm = text.toLowerCase();
    const filtered = PRODUCTS.filter(product =>
      product.name.toLowerCase().includes(searchTerm) ||
      product.category.toLowerCase().includes(searchTerm) ||
      product.price.toString().includes(searchTerm)
    );
    setResults(filtered);
  };

  const renderProduct = ({ item }: { item: Product }) => (
    <TouchableOpacity 
      onPress={() => setSelectedImage(item.image)}
      activeOpacity={0.7}
    >
      <ThemedView style={styles.productCard}>
        <Image 
          source={{ uri: item.image }}
          style={styles.productImage}
          resizeMode="cover"
        />
        <ThemedText style={styles.productName}>{item.name}</ThemedText>
        <ThemedText style={styles.productPrice}>${item.price}</ThemedText>
        <ThemedText style={styles.productCategory}>{item.category}</ThemedText>
      </ThemedView>
    </TouchableOpacity>
  );

  return (
    <ThemedView style={styles.container}>
      <ThemedView style={styles.searchContainer}>
        <TextInput
          style={styles.searchInput}
          value={searchQuery}
          onChangeText={handleSearch}
          placeholder="Search products..."
          placeholderTextColor="#666"
        />
        <Ionicons 
          name="search" 
          size={24} 
          color="#666" 
          style={styles.searchIcon}
        />
      </ThemedView>
      
      <FlatList
        data={results}
        renderItem={renderProduct}
        keyExtractor={(item) => item.id}
        style={styles.list}
      />

      <Modal
        visible={!!selectedImage}
        transparent={true}
        onRequestClose={() => setSelectedImage(null)}
        animationType="fade"
      >
        <TouchableOpacity 
          style={styles.modalOverlay}
          activeOpacity={1}
          onPress={() => setSelectedImage(null)}
        >
          {selectedImage && (
            <Image
              source={{ uri: selectedImage }}
              style={styles.enlargedImage}
              resizeMode="contain"
            />
          )}
        </TouchableOpacity>
      </Modal>
    </ThemedView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  searchContainer: {
    position: 'relative',
    marginBottom: 16,
  },
  searchInput: {
    height: 50,
    borderRadius: 8,
    paddingHorizontal: 16,
    paddingRight: 46,
    borderWidth: 1,
    borderColor: '#ccc',
    color: 'white',
  },
  searchIcon: {
    position: 'absolute',
    right: 12,
    top: 12,
  },
  list: {
    flex: 1,
  },
  productCard: {
    padding: 16,
    marginBottom: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#ccc',
  },
  productName: {
    fontSize: 18,
    marginBottom: 4,
  },
  productPrice: {
    fontSize: 16,
    marginBottom: 4,
  },
  productCategory: {
    fontSize: 14,
    opacity: 0.7,
  },
  productImage: {
    width: '100%',
    height: 200,
    borderRadius: 8,
    marginBottom: 8,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  enlargedImage: {
    width: Dimensions.get('window').width * 0.9,
    height: Dimensions.get('window').height * 0.7,
    borderRadius: 12,
  },
}); 