import { Tabs } from 'expo-router';
import React from 'react';
import { TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

import { TabBarIcon } from '@/components/navigation/TabBarIcon';
import { useColorScheme } from '@/hooks/useColorSchemeContext';

export default function TabLayout() {
  const { colorScheme, toggleColorScheme } = useColorScheme();

  return (
    <Tabs
      screenOptions={{
        // Set tab bar colors based on color scheme
        tabBarStyle: {
          backgroundColor: colorScheme === 'dark' ? '#151718' : '#fff',
        },
        tabBarActiveTintColor: colorScheme === 'dark' ? '#fff' : '#0a7ea4',
        headerStyle: {
          backgroundColor: colorScheme === 'dark' ? '#151718' : '#fff',
        },
        headerRight: () => (
          // Theme toggle button in header
          <TouchableOpacity 
            onPress={toggleColorScheme} 
            style={{ marginRight: 15 }}
          >
            <Ionicons
              name={colorScheme === 'dark' ? 'sunny' : 'moon'}
              size={24}
              color={colorScheme === 'dark' ? '#fff' : '#0a7ea4'}
            />
          </TouchableOpacity>
        ),
        headerTintColor: colorScheme === 'dark' ? '#fff' : '#000',
      }}>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'home' : 'home-outline'} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="search"
        options={{
          title: 'Search',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'search' : 'search-outline'} color={color} />
          ),
        }}
      />
    </Tabs>
  );
}
