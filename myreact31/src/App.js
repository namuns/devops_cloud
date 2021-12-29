import PageLotto from "./Page/PageLotto";
// import { useState } from "react";
import ProfileCard from "./Page/ProfileCard";
import "./Page/ProfileCard.css";
import Axios from "axios";
const { useState, useEffect } = require("react");

function App() {
  const [profileList, setProfileList] = useState([]);

  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const [pageName, setPageName] = useState("진");

  return (
    <div>
      {profileList.map((member, index) => {
        // const className = memberNoList[(index % 4) + 1];
        const className = `member${(index % 4) + 1}`;
        if (pageName === member.name) {
          return (
            <ProfileCard
              name={member.name}
              role={member.role}
              mbti={member.mbti}
              instagram_url={member.instagram_url}
              profile_image_url={member.profile_image_url}
            >
              {profileList.map((member) => {
                return (
                  <a
                    className={pageName == member.name ? "on" : ""}
                    onClick={() => setPageName(member.name)}
                  ></a>
                );
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
