// import Cartoons from "./components/Cartoons";
import Cartoon from "./components/tempCartoon";
import Button from "./components/Button";
const App = () =>  
{
const car = [
  {
    name: "Doraemon",
    creator: "Fujiko F. Fujio",
    year: 1969,
    mainCharacter: "Doraemon",
    genre: "Sci-Fi, Comedy",
    image: "https://upload.wikimedia.org/wikipedia/en/0/0f/Doraemon_character.png"
  },
  {
    name: "Shinchan",
    creator: "Yoshito Usui",
    year: 1990,
    mainCharacter: "Shinchan",
    genre: "Comedy",
    image: "https://upload.wikimedia.org/wikipedia/en/7/7d/Shinchan.png"
  },
  {
    name: "Tom and Jerry",
    creator: "William Hanna & Joseph Barbera",
    year: 1940,
    mainCharacter: "Tom & Jerry",
    genre: "Comedy",
    image: "https://upload.wikimedia.org/wikipedia/en/f/f6/Tom_and_Jerry.png"
  },
  {
    name: "Pokemon",
    creator: "Satoshi Tajiri",
    year: 1997,
    mainCharacter: "Ash Ketchum",
    genre: "Adventure, Fantasy",
    image: "https://upload.wikimedia.org/wikipedia/en/3/39/Ash_Ketchum_Sun_and_Moon.png"
  },
  {
    name: "Ben 10",
    creator: "Man of Action",
    year: 2005,
    mainCharacter: "Ben Tennyson",
    genre: "Action, Sci-Fi",
    image: "https://upload.wikimedia.org/wikipedia/en/9/9b/Ben_10_Alien_Force.png"
  }
];

  return (
    <div className="grid grid-cols- md:grid-cols-2 lg:grid-cols-3 m-auto max-w-4xl gap-5">
      <Button size="50px" color="red" text="Signup " />
      {
        car.map((val, index) => (
          <Cartoon
            key={index}
            imgLink={val.image}
            name1={val.name}
          />
        ))
        
      }


    </div>
  )
}

export default App;