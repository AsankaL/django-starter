import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = ['output']
  connect() {
    console.log("Hello, Stimulus!", this.element)
  }

  greet(){
    this.outputTarget.innerHTML = 'Hi there!'
  }
}