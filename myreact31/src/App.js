import PageLotto from "./Page/PageLotto";
import { useState } from "react";
import ProfileCard from "./Page/ProfileCard";
import "./Page/ProfileCard.css";
import profileImage1 from "./img/member1.jpg";
import profileImage2 from "./img/member2.jpg";
import profileImage3 from "./img/member3.jpg";
import profileImage4 from "./img/member4.jpg";
// import member from './Page/memberInfo.json'

function App() {
  const [pageName, setPageName] = useState("member1");

  return (
    <div>
      {pageName == "member1" ? (
        <ProfileCard
          name="Jane"
          role="UI/UX INTERACTIVE DEVELOPER"
          profileImage={profileImage1}
          facebook_url="facebook.com/jane"
          email="jane@gmail.com"
          changePageName={setPageName}
        />
      ) : pageName == "member2" ? (
        <ProfileCard
          name="Kevin"
          role="Jane"
          profileImage={profileImage2}
          facebook_url="member.facebook_url"
          email="member.email"
          changePageName={setPageName}
        />
      ) : pageName == "member3" ? (
        <ProfileCard
          name="John"
          role="Jane"
          profileImage={profileImage3}
          facebook_url="member.facebook_url"
          email="member.email"
          changePageName={setPageName}
        />
      ) : (
        <ProfileCard
          name="qwerty"
          role="Jane"
          profileImage={profileImage4}
          facebook_url="member.facebook_url"
          email="member.email"
          changePageName={setPageName}
        />
      )}

      <PageLotto />
    </div>
  );
}
export default App;
