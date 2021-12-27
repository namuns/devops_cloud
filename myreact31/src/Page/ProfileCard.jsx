import profileImage from "../img/member1.jpg";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faStickyNote } from "@fortawesome/free-solid-svg-icons";

function ProfileCard({
  profileImage,
  name,
  role,
  facebook_url,
  email,
  changePageName,
}) {
  return (
    <div>
      <h2>Profile Card</h2>
      <>
        <section>
          <nav className="menu">
            <a href="#">
              <FontAwesomeIcon icon={faBars} />
            </a>
            <a href="#">
              <FontAwesomeIcon icon={faStickyNote} />
            </a>
          </nav>
          <article className="profile">
            <img src={profileImage} alt="프로필 이미지" />
            <h1>{name}</h1>
            <h2>{role}</h2>
            <a href="#" className="btnView">
              VIEW MORE
            </a>
          </article>
          <ul className="contact">
            <li>
              <i className="fab fa-facebook-f" />
              <span>{facebook_url}</span>
            </li>
            <li>
              <i className="fas fa-envelope" />
              <span>{email}</span>
            </li>
          </ul>
          <nav className="others">
            <li>
              <a onClick={() => changePageName("about")}></a>
            </li>
            <li>
              <a onClick={() => changePageName("counter")}></a>
            </li>
            <li>
              <a onClick={() => changePageName("lotto")}></a>
            </li>
            <li>
              <a onClick={() => changePageName("playlist")}></a>
            </li>
          </nav>
        </section>
      </>
    </div>
  );
}

export default ProfileCard;
