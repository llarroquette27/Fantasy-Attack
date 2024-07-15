const Menu = () => {
    const nflLogo = '/nfl.png'
    const home = '/home.svg'
    const team = '/team.svg'
    const pos = '/pos.svg'
    const search = '/search.svg'
  return (
     <div className='menu'>
        <img src={nflLogo} className="logo"></img>
        <img src={home} className="logo"></img>
        <img src={team} className="logo"></img>
        <img src={pos} className="logo"></img>
        <img src={search} className="logo"></img>
    </div>
  )
}

export default Menu
