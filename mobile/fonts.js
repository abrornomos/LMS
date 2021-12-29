import * as Font from 'expo-font'


export const fonts = () => Font.loadAsync({
  'os-bold': require('./assets/fonts/OpenSans-Bold.ttf'),
  'os-light': require('./assets/fonts/OpenSans-Light.ttf'),
  'os-regular': require('./assets/fonts/OpenSans-Regular.ttf')
})