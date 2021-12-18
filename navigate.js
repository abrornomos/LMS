import React from 'react'
import Main from './components/Main'
import Contact from './components/Contact'

import { createStackNavigator } from '@react-navigation/stack'
import { NavigationContainer } from '@react-navigation/native'

const Stack = createStackNavigator()

export default function Navigate() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Main" component={Main} options={{title: "Главная страница"}} />
        <Stack.Screen name="Contact" component={Contact} options={{title: "О нас"}} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}