import axios from 'axios';

const HomePageButton = () => {
  return (
    <button className="homePageButton" onClick={() => {
      axios.get('http://localhost:3000')
    .then(res => console.log(res.data))
    }}>
        Start now!
    </button>
  )
}

export default HomePageButton
