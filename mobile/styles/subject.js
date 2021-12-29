import { StyleSheet } from "react-native"

export const subjectStyle = StyleSheet.create({
  mainContainer: {
    padding: 20,
    marginVertical: 30,
    marginHorizontal: 15,
    backgroundColor: "#ffffff"
  },
  tableRow: {
    padding: 15,
    display: "flex",
    alignSelf: "stretch",
    flexDirection: "row"
  },
  tableHeadElementText: {
    fontFamily: "os-bold"
  },
  tableRowElements: {
    flex: 1,
    alignSelf: "stretch"
  },
  hr: {
    borderBottomColor: "black",
    borderBottomWidth: 1
  }
})
