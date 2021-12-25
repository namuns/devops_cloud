import { useState } from "react";
import TopNav from "components/TopNav";
import PageAbout from "pages/PageAbout";
import PageCounter from "pages/PageCounter";
import PageLotto from "pages/PageLotto";
import PagePlayList from "pages/PagePlayList";

function App() {
  const [pageName, setPageName] = useState("about");

  // const changePageName = (pageName) => {
  //     setPageName(pageName);
  //   }


  return(
    <div>
      <h1>React</h1>
      <TopNav changePageName={setPageName}/>
      {pageName === "about" && <PageAbout/>}
      {pageName === "counter" && <PageCounter/>}
      {pageName === "lotto" && <PageLotto/>}
      {pageName === "playlist" && <PagePlayList/>}
      
    </div>
  );
}

export default App;