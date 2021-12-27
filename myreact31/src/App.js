import PageLotto from './Page/PageLotto';
import { useState } from "react";
import ProfileCard from './Page/ProfileCard';
import './Page/ProfileCard.css'

function App() {


  return(
    <div>
    <ProfileCard
      profileImage={123}
      name={123}
      role={123}
      facebook_url={123}
      email={123} />
    <ProfileCard
      profileImage={123}
      name={123}
      role={123}
      facebook_url={123}
      email={123} />
    <ProfileCard
      profileImage={123}
      name={123}
      role={123}
      facebook_url={123}
      email={123} />
    <ProfileCard
      profileImage={123}
      name={123}
      role={123}
      facebook_url={123}
      email={123}></ProfileCard>
      <PageLotto/>
    </div>
  )
  }
export default App;
