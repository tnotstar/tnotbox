// const buttonElm = document.querySelector('button')
// const inputElm = document.querySelector('input')
// const listElm = document.querySelector('ul')

// function addGoal() {
//   const enteredValue = inputElm.value
//   if (enteredValue) {
//     const listItemElm = document.createElement('li')
//     listElm.appendChild(listItemElm)
//     listItemElm.textContent = enteredValue
//     inputElm.value = null
//   }
//   inputElm.focus()
// }

// buttonElm.addEventListener('click', addGoal)

Vue.createApp({
  data: () => {
    return {
      goals: [],
      enteredValue: ''
    }
  },
  methods: {
    addGoal() {
      this.goals.push(this.enteredValue)
    }

  }
}).mount('#app')
