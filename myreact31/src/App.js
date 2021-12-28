import PageLotto from "./Page/PageLotto";
import { useState } from "react";
import ProfileCard from "./Page/ProfileCard";
import "./Page/ProfileCard.css";
import profileImage1 from "./img/member1.jpg";
import profileImage2 from "./img/member2.jpg";
import profileImage3 from "./img/member3.jpg";
import profileImage4 from "./img/member4.jpg";
import members from "./Page/memberInfo.json";

function App() {
  const [pageName, setPageName] = useState("member1");

  return (
    <div>
      {members.map((member) => {
        if (pageName === member.member) {
          return (
            <ProfileCard
              name={member.name}
              role={member.role}
              facebook_url={member.facebook_url}
              email={member.email}
              profileImage={profileImage1}
              changePageName={setPageName}
            />
          );
        }
      })}

      <PageLotto />
    </div>
  );
}
export default App;
