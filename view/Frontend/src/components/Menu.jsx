import { Link } from 'react-router-dom';
import '../index.css'

const Menu = () => {
    const nflLogo = '/nfl.png'
    const home = '/home.svg'
    const team = '/team.svg'
    const pos = '/pos.svg'
    const search = '/search.svg'
  return (
     <div className='menu'>
        <img src={nflLogo} className="logo" id="nfl"></img>
        <Link to='/'><img src={home} className="logo"></img></Link>
        <Link to='/teams'><img src={team} className="logo"></img></Link>
        <Link to='/pos'><img src={pos} className="logo"></img></Link>
        <Link to='/search'><img src={search} className="logo"></img></Link>
    </div>
  )
}

export default Menu
