import React from 'react';
import { WebView } from 'react-native-webview';
import { SafeAreaView, StatusBar, StyleSheet, View, Text } from 'react-native';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#1E1E2C" />
      
      {/* 
        దయచేసి కింద ఉన్న లింక్ ని తీసివేసి మీ అసలైన Railway లింక్ పెట్టండి 
        Please replace the uri below with your actual Railway link 
      */}
      <WebView 
         source={{ uri: 'https://oralcancer-production.up.railway.app' }} 
         style={{ flex: 1 }} 
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
