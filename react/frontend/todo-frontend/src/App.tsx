import { useState } from 'react'
import './App.css'

function App() {
  const [tasks, setTasks] = useState<string[]>([])
  const [input, setInput] = useState('')

  const addTask = () => {
    if (input.trim() === '') return
    setTasks(prevTasks => [...prevTasks, input])
    setInput('')
  }

  const deleteTask = (index: number) => {
    setTasks(prevTasks => prevTasks.filter((_, i) => i !== index))
  }

  return (

    <div>
      <h1>ToDo App. (React)</h1>

      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder='タスクを入力'
        />

      <button className="add_button" onClick={addTask}>追加</button>

      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task}
            <button className='delete_button' onClick={() => deleteTask(index)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
