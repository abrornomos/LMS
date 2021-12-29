import React, { useState } from 'react'
import { StyleSheet } from 'react-native'
import AppLoading from 'expo-app-loading'
import MainStack from './navigate'
import { fonts } from './fonts'

export default function App() {
  const [font, setFont] = useState(false)
  if (font) {
    return (
      <MainStack />
    )
  } else {
    return (
      <AppLoading startAsync={fonts} onFinish={() => setFont(true)} onError={console.warn} />
    )
  }
}

const styles = StyleSheet.create({
  
})
