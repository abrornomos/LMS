import React, { useState } from 'react'
import AppLoading from 'expo-app-loading'
import { fonts } from './fonts'
import Dashboard from './components/Dashboard'
import Subjects from './components/Subjects'
import Schedule from './components/Schedule'
import ISP from './components/ISP'
import Information from './components/Information'

import { createStackNavigator } from '@react-navigation/stack'
import { createDrawerNavigator } from '@react-navigation/drawer'
import { NavigationContainer } from '@react-navigation/native'

const Stack = createStackNavigator()
const Drawer = createDrawerNavigator()

// function MainStack() {
//   return (
//       <Stack.Navigator>
//         <Stack.Screen name="Main" component={Main} options={{
//           headerShown: false
//         }} />
//         <Stack.Screen name="FullInfo" component={FullInfo} options={{
//           headerShown: false
//         }} />
//       </Stack.Navigator>
//   )
// }


//Abror nima gap? Oxshayaptimi?????



function DrawerScreenHeaderOptions(title) {
  return {
    drawerItemStyle: {
      color: "#fff"
    },
    title: title,
    headerStyle: {
      backgroundColor: '#262859',
    },
    headerTintColor: '#fff',
    headerTitleStyle: {
      fontFamily: "os-regular"
    }
  }
}

export default function Navigate() {
  const [font, setFont] = useState(false)
  if (font) {
    return (
      <NavigationContainer>
        <Drawer.Navigator screenOptions={{
          drawerStyle: {
            backgroundColor: "#262859"
          },
          drawerLabelStyle: {
            color: "#fff"
          }
        }}>
          <Drawer.Screen name="Dashboard" component={Dashboard} options={() => DrawerScreenHeaderOptions("Лента")} />
          <Drawer.Screen name="Subjects" component={Subjects} options={() => DrawerScreenHeaderOptions("Мои предметы")} />
          <Drawer.Screen name="Schedule" component={Schedule} options={() => DrawerScreenHeaderOptions("Расписание")} />
          <Drawer.Screen name="ISP" component={ISP} options={() => DrawerScreenHeaderOptions("Индивидуальный учебный план")} />
          <Drawer.Screen name="Information" component={Information} options={() => DrawerScreenHeaderOptions("Информация")} />
        </Drawer.Navigator>
        
      </NavigationContainer>
    )
  } else {
    return (
      <AppLoading startAsync={fonts} onFinish={() => setFont(true)} onError={console.warn} />
    )
  }
}
