import PageLotto from "./Page/PageLotto";
import { useState } from "react";
import ProfileCard from "./Page/ProfileCard";
import "./Page/ProfileCard.css";
import members from "./Page/memberInfo.json";

const memberNoList = members.map(({ memberNo }) => memberNo);

function App() {
  const [pageName, setPageName] = useState(memberNoList[0]);

  return (
    <div>
      {members.map((member, index) => {
        // const className = memberNoList[(index % 4) + 1];
        const className = `member${(index % 4) + 1}`;
        if (pageName === member.memberNo) {
          return (
            <ProfileCard
              memberNo={member.memberNo}
              name={member.name}
              role={member.role}
              facebook_url={member.facebook_url}
              email={member.email}
              className={className}
            >
              {memberNoList.map((id) => {
                return <a onClick={() => setPageName(id)}></a>;
              })}
            </ProfileCard>
          );
        }
      })}

      <PageLotto />
    </div>
  );
}
export default App;
