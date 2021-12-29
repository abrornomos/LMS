import React, { useEffect, useState } from 'react'
import { StyleSheet, Text, View } from 'react-native'
import { gStyle } from '../styles/style'
import { subjectStyle } from '../styles/subject'
import axios from "axios"

const baseUrl = "http://127.0.0.1:5000"

function SubjectElements(subject, key) {
  return (
    <View key={key} style={subjectStyle.tableRow}>
      <View style={subjectStyle.tableRowElements}>
        <Text>{subject.name}</Text>
      </View>
    </View>
  )
}

export default function Subjects() {

  const [subjects, setSubjects] = useState([])

  useEffect(() => {
    axios.get(`${baseUrl}/subject/`).then(response => {
      const results = response.data
      setSubjects(results)
      // subjects = response.data
      // console.log(subjects)
    })
  }, []);
  return (
    <View style={gStyle.main}>
      <Text style={gStyle.title}>Мои предметы</Text>
      <View style={subjectStyle.mainContainer}>
        <View style={subjectStyle.tableRow}>
          <View style={subjectStyle.tableRowElements}>
            <Text style={subjectStyle.tableHeadElementText}>Дисциплина</Text>
            <Text style={subjectStyle.tableHeadElementText}>Преподаватель</Text>
            <Text style={subjectStyle.tableHeadElementText}>Кол-во НБ</Text>
            <Text style={subjectStyle.tableHeadElementText}>Действие</Text>
          </View>
        </View>
        <View style={subjectStyle.hr}/>
        {
          subjects.map((subject) => {
            return SubjectElements(subject, Math.random().toString(36).substr(2, 9))
          })
        }
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  
})
