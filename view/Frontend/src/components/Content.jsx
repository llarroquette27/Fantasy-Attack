import HomePageButton from "../components/HomePageButton"

const Content = () => {
    const nflLogo = '/nfl.png'
    return (
    <div className='content'>
        <div className="mainContent">
            <img src={nflLogo} id="largeLogo"></img>
            <p className='description'>Welcome to Fantasy Attack!</p>
            <p className="smallDescription">The ultimate site for everything fantasy football related. Click the button to begin!</p>
            <HomePageButton />
        </div>
    </div>
  )
}

export default Content
