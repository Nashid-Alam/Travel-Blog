import "./App.css"
import { Route, Switch } from "react-router-dom"
import Cities from "./Pages/Cities"
import Blogs from "./Pages/Blogs"

function App() {
  return (
    <div className="App">
      <main>
        <Switch>
          <Route exact path="/" component={Cities} />
          <Route exact path="/blogs/:city_id" component={Blogs} />
        </Switch>
      </main>
    </div>
  )
}

export default App
