import React, { useState, useEffect } from 'react';

// --- DATA: 50 Questions (Flawless Array Syntax) ---
const quizData = [
  // TYPE 1: Fill-in-the-blank (35 questions)
  { type: "blank", emoji: "🌧️🏖️", english: "_____ it rains heavily in the summer, Miami is always full of tourists.", spanish: "Aunque llueve mucho en el verano, Miami siempre está llena de turistas.", options: ["Although", "Despite", "Because", "Therefore"], correct: 0, explanation: "Use 'Although' before a subject + verb clause (it rains)." },
  { type: "blank", emoji: "🚗🌴", english: "We decided to go to South Beach _____ the heavy traffic.", spanish: "Decidimos ir a South Beach a pesar del tráfico pesado.", options: ["Although", "However", "Despite", "Because of"], correct: 2, explanation: "Use 'Despite' before a noun phrase ('the heavy traffic') to show contrast." },
  { type: "blank", emoji: "🎨📸", english: "The Wynwood Walls are famous worldwide _____ their amazing street art.", spanish: "Las Wynwood Walls son famosas en todo el mundo por su increíble arte callejero.", options: ["because", "because of", "since", "therefore"], correct: 1, explanation: "Use 'because of' before a noun phrase. 'Because' requires a full subject + verb clause." },
  { type: "blank", emoji: "🥪🚪", english: "I wanted to eat a Cuban sandwich in Little Havana; _____, the restaurant was closed.", spanish: "Quería comer un sándwich cubano; sin embargo, el restaurante estaba cerrado.", options: ["Although", "Moreover", "However", "Despite"], correct: 2, explanation: "'However' is used to introduce a contrasting statement, often following a semicolon." },
  { type: "blank", emoji: "💸🍹", english: "The club in Downtown was extremely expensive. _____, we went to a cheaper bar on Ocean Drive.", spanish: "El club era extremadamente caro. Por lo tanto, fuimos a un bar más barato.", options: ["Therefore", "Although", "Because", "Instead of"], correct: 0, explanation: "'Therefore' shows consequence or result." },
  { type: "blank", emoji: "🏖️🎉", english: "Miami has beautiful white-sand beaches. _____, it offers an excellent nightlife scene.", spanish: "Miami tiene hermosas playas. Además, ofrece una excelente vida nocturna.", options: ["Although", "Therefore", "Moreover", "Despite"], correct: 2, explanation: "'Moreover' is used to add more information that supports the previous point." },
  { type: "blank", emoji: "🚕🚤", english: "_____ taking a taxi, we rented a boat to see the mansions on Star Island.", spanish: "En lugar de tomar un taxi, alquilamos un bote.", options: ["Despite", "Instead of", "Because of", "However"], correct: 1, explanation: "'Instead of' means in place of something else. It's followed by a noun or gerund (-ing)." },
  { type: "blank", emoji: "🐊💦", english: "The Everglades airboat ride was cancelled _____ the approaching hurricane.", spanish: "El paseo fue cancelado debido al huracán que se aproximaba.", options: ["due to", "since", "although", "therefore"], correct: 0, explanation: "'Due to' means 'caused by' or 'because of' and is followed by a noun phrase." },
  { type: "blank", emoji: "🛍️😎", english: "She bought a lot of designer clothes at Bayside Marketplace _____ they were very expensive.", spanish: "Compró mucha ropa a pesar de que (aunque) era muy cara.", options: ["despite", "even though", "because", "instead of"], correct: 1, explanation: "'Even though' is similar to 'although' and is followed by a subject + verb clause." },
  { type: "blank", emoji: "☕🥱", english: "We drank three shots of Cuban coffee; _____, we were still tired from the flight.", spanish: "Tomamos tres tragos de café; aun así, todavía estábamos cansados.", options: ["nevertheless", "therefore", "because", "moreover"], correct: 0, explanation: "'Nevertheless' is a formal way to say 'however' or 'in spite of that'." },
  { type: "blank", emoji: "☀️🕶️", english: "_____ we are already in Miami, let's go swimming at South Pointe Park.", spanish: "Ya que estamos en Miami, vamos a nadar a South Pointe Park.", options: ["Although", "Since", "Unless", "Therefore"], correct: 1, explanation: "'Since' can mean 'because' or 'as', giving a reason for the following suggestion." },
  { type: "blank", emoji: "🎟️🛑", english: "We won't go to the electronic music festival _____ you buy the VIP tickets.", spanish: "No iremos al festival a menos que compres las entradas VIP.", options: ["because", "unless", "if", "despite"], correct: 1, explanation: "'Unless' means 'except if' and introduces a condition." },
  { type: "blank", emoji: "🏙️🌴", english: "Ocean Drive is very loud and crowded, _____ Coral Gables is quite peaceful and quiet.", spanish: "Ocean Drive es muy ruidoso, mientras que Coral Gables es bastante tranquilo.", options: ["whereas", "because", "therefore", "unless"], correct: 0, explanation: "'Whereas' is used to contrast two facts or ideas." },
  { type: "blank", emoji: "🐬🚤", english: "_____ I was riding the jet ski, I saw a beautiful dolphin jump out of the water.", spanish: "Mientras conducía la moto acuática, vi un hermoso delfín.", options: ["During", "While", "Despite", "Since"], correct: 1, explanation: "'While' is followed by a subject and a continuous verb to show two things happening at once." },
  { type: "blank", emoji: "💃🍹", english: "Miami is famous for its vibrant nightlife _____ its incredible Latin American cuisine.", spanish: "Miami es famosa por su vida nocturna así como por su increíble cocina.", options: ["as well as", "therefore", "because", "however"], correct: 0, explanation: "'As well as' means 'in addition to' or 'and'." },
  { type: "blank", emoji: "💸🛌", english: "I don't want to go to the club tonight; _____, I don't have enough money.", spanish: "No quiero ir al club; además, no tengo suficiente dinero.", options: ["besides", "although", "despite", "therefore"], correct: 0, explanation: "'Besides' introduces an additional, often more decisive, point or reason." },
  { type: "blank", emoji: "🏛️🌴", english: "The Art Deco architecture is historically significant. _____, it provides a beautiful backdrop for photos.", spanish: "La arquitectura es históricamente significativa. Además, proporciona un hermoso fondo.", options: ["However", "Furthermore", "Although", "Despite"], correct: 1, explanation: "'Furthermore' is used to add another supportive point to an argument." },
  { type: "blank", emoji: "🥵🍦", english: "It was incredibly hot walking around Brickell, _____ we stopped to buy some gelato.", spanish: "Hacía un calor increíble, así que nos detuvimos a comprar helado.", options: ["so", "because", "although", "unless"], correct: 0, explanation: "'So' introduces the result or consequence of a situation." },
  { type: "blank", emoji: "⛈️🏄‍♂️", english: "We had a fantastic time at the beach _____ the unexpected afternoon thunderstorm.", spanish: "Nos lo pasamos genial en la playa a pesar de la inesperada tormenta.", options: ["although", "in spite of", "because", "however"], correct: 1, explanation: "'In spite of' functions exactly like 'despite' and is followed by a noun." },
  { type: "blank", emoji: "😎💦", english: "_____ he loves the Miami lifestyle, he absolutely hates the summer humidity.", spanish: "Aunque ama el estilo de vida de Miami, odia la humedad del verano.", options: ["Despite", "Because", "Although", "Therefore"], correct: 2, explanation: "'Although' must be followed by a full clause (he loves)." },
  { type: "blank", emoji: "🥱💃", english: "_____ being exhausted from the flight, she danced salsa all night in Little Havana.", spanish: "A pesar de estar exhausta por el vuelo, bailó salsa toda la noche.", options: ["Although", "Because", "Despite", "However"], correct: 2, explanation: "'Despite' can be followed by a gerund (-ing verb)." },
  { type: "blank", emoji: "🏨🛎️", english: "The hotel had a great pool. _____, the customer service was extremely slow.", spanish: "El hotel tenía una gran piscina. Sin embargo, el servicio fue lento.", options: ["Moreover", "However", "Because", "Therefore"], correct: 1, explanation: "'However' introduces a contrast to the previous sentence." },
  { type: "blank", emoji: "☕❤️", english: "I always visit Calle Ocho _____ they serve the best cortaditos in the city.", spanish: "Siempre visito la Calle Ocho porque sirven los mejores cortaditos.", options: ["because", "because of", "although", "unless"], correct: 0, explanation: "'Because' is a conjunction followed by a subject and a verb (they serve)." },
  { type: "blank", emoji: "✈️🕒", english: "Our flight to Miami International was delayed; _____, we missed our dinner reservation.", spanish: "Nuestro vuelo se retrasó; por lo tanto, perdimos nuestra reserva.", options: ["however", "therefore", "although", "despite"], correct: 1, explanation: "'Therefore' shows the logical result of the flight being delayed." },
  { type: "blank", emoji: "🎨🛍️", english: "The Design District is known for luxury fashion. _____, it features incredible modern art installations.", spanish: "El Design District es conocido por la moda. Además, presenta increíbles instalaciones de arte.", options: ["Moreover", "However", "Therefore", "Despite"], correct: 0, explanation: "'Moreover' adds related positive information." },
  { type: "blank", emoji: "☀️🧴", english: "_____ the Florida sun is extremely strong, you must wear SPF 50 sunscreen.", spanish: "Dado que el sol de Florida es muy fuerte, debes usar protector solar.", options: ["Although", "Since", "Unless", "Despite"], correct: 1, explanation: "'Since' here means 'because of the fact that'." },
  { type: "blank", emoji: "🚗🅿️", english: "Do not park on Ocean Drive _____ you want to get a $100 parking ticket.", spanish: "No estaciones en Ocean Drive a menos que quieras una multa de $100.", options: ["because", "unless", "if", "although"], correct: 1, explanation: "'Unless' means 'except if'." },
  { type: "blank", emoji: "🏖️🧘‍♀️", english: "North Beach is very calm and family-friendly, _____ South Beach is energetic and loud.", spanish: "North Beach es muy tranquila, mientras que South Beach es enérgica.", options: ["whereas", "because", "since", "therefore"], correct: 0, explanation: "'Whereas' connects two contrasting ideas in one sentence." },
  { type: "blank", emoji: "🚶‍♂️🦜", english: "_____ walking along the Venetian Causeway, we saw a group of wild parrots.", spanish: "Mientras caminábamos por la calzada, vimos loros salvajes.", options: ["During", "While", "Because", "Despite"], correct: 1, explanation: "'While' is used with an -ing verb to show an action in progress." },
  { type: "blank", emoji: "🗣️🌎", english: "To work in Miami retail, it helps to speak English _____ Spanish fluently.", spanish: "Para trabajar en tiendas, ayuda hablar inglés así como español fluidamente.", options: ["as well as", "therefore", "because", "however"], correct: 0, explanation: "'As well as' means 'and in addition'." },
  { type: "blank", emoji: "🥱🏠", english: "I don't feel like going out to the club; _____, I have to wake up early for a boat tour tomorrow.", spanish: "No tengo ganas de salir; además, tengo que despertarme temprano mañana.", options: ["besides", "although", "despite", "so"], correct: 0, explanation: "'Besides' adds an extra, often conclusive, reason." },
  { type: "blank", emoji: "🛥️💵", english: "The boat tour was surprisingly affordable. _____, the tour guide was hilarious and informative.", spanish: "El tour fue asequible. Además, el guía fue muy divertido e informativo.", options: ["Furthermore", "However", "Although", "Therefore"], correct: 0, explanation: "'Furthermore' adds more positive information." },
  { type: "blank", emoji: "🐊📸", english: "We really wanted to take pictures of alligators, _____ we drove out to the Everglades.", spanish: "Queríamos tomar fotos de caimanes, así que condujimos a los Everglades.", options: ["so", "because", "although", "unless"], correct: 0, explanation: "'So' links a desire to the action taken to fulfill it." },
  { type: "blank", emoji: "🚶‍♂️🚶‍♀️", english: "_____ the massive line outside, we decided to wait to get into the famous nightclub.", spanish: "A pesar de la enorme fila afuera, decidimos esperar para entrar al club.", options: ["In spite of", "Although", "Because", "However"], correct: 0, explanation: "'In spite of' is followed by a noun phrase ('the massive line')." },
  { type: "blank", emoji: "🌪️✈️", english: "All flights out of MIA were cancelled _____ the severe tropical storm warnings.", spanish: "Todos los vuelos fueron cancelados debido a las advertencias de tormenta.", options: ["because of", "because", "although", "despite"], correct: 0, explanation: "'Because of' is followed by a noun phrase explaining the reason." },

  // TYPE 2: Correct Usage (15 questions)
  { type: "usage", emoji: "🤔🌴", english: "Choose the correct sentence using 'However'.", spanish: "Significado: El club estaba abierto; sin embargo, estaba vacío.", options: [
      "The club was open however it was empty.",
      "The club was open, however it was empty.",
      "The club was open; however, it was empty.",
      "However the club was open, it was empty."
  ], correct: 2, explanation: "'However' connects two independent clauses and usually follows a semicolon or period, and is followed by a comma." },
  { type: "usage", emoji: "🤔🥵", english: "Choose the correct sentence using 'Although'.", spanish: "Significado: Aunque hacía mucho calor, caminamos por Wynwood.", options: [
      "Although it was very hot, we walked around Wynwood.",
      "Although being very hot, we walked around Wynwood.",
      "We walked around Wynwood. Although it was very hot.",
      "Although the heat, we walked around Wynwood."
  ], correct: 0, explanation: "'Although' must be followed by a full subject and verb clause ('it was')." },
  { type: "usage", emoji: "🤔⛈️", english: "Choose the correct sentence using 'Despite'.", spanish: "Significado: A pesar de la lluvia, la fiesta en la piscina continuó.", options: [
      "Despite it rained, the pool party continued.",
      "Despite of the rain, the pool party continued.",
      "The pool party continued despite, the rain.",
      "Despite the rain, the pool party continued."
  ], correct: 3, explanation: "'Despite' is followed by a noun ('the rain'). It never takes 'of' and isn't followed by a comma." },
  { type: "usage", emoji: "🤔🛍️", english: "Choose the correct sentence using 'In spite of'.", spanish: "Significado: Ella compró el vestido a pesar del alto precio.", options: [
      "She bought the dress in spite of the high price.",
      "She bought the dress in spite the high price.",
      "In spite of it was expensive, she bought the dress.",
      "She bought the dress in spite of, the high price."
  ], correct: 0, explanation: "'In spite of' is always three words and is followed by a noun phrase." },
  { type: "usage", emoji: "🤔❄️", english: "Choose the correct sentence using 'Because'.", spanish: "Significado: Entramos porque el aire acondicionado estaba encendido.", options: [
      "We went inside because of the AC was on.",
      "We went inside because the AC was on.",
      "Because the AC, we went inside.",
      "We went inside, because, the AC was on."
  ], correct: 1, explanation: "'Because' is a conjunction connecting two clauses, followed by a subject and verb." },
  { type: "usage", emoji: "🤔💸", english: "Choose the correct sentence using 'Therefore'.", spanish: "Significado: Olvidé mi billetera; por lo tanto, no pude comprar el mojito.", options: [
      "I forgot my wallet therefore I couldn't buy the mojito.",
      "I forgot my wallet, therefore, I couldn't buy the mojito.",
      "I forgot my wallet; therefore, I couldn't buy the mojito.",
      "Therefore I forgot my wallet, I couldn't buy the mojito."
  ], correct: 2, explanation: "'Therefore' is a conjunctive adverb. It requires a semicolon (or a new sentence) before it and a comma after it." },
  { type: "usage", emoji: "🤔🏖️", english: "Choose the correct sentence using 'So'.", spanish: "Significado: La playa estaba llena, así que fuimos a la piscina del hotel.", options: [
      "The beach was crowded, so we went to the hotel pool.",
      "The beach was crowded so, we went to the hotel pool.",
      "So the beach was crowded, we went to the hotel pool.",
      "The beach was crowded; so we went to the hotel pool."
  ], correct: 0, explanation: "'So' is a coordinating conjunction. It links two independent clauses and is preceded by a comma." },
  { type: "usage", emoji: "🤔🥟", english: "Choose the correct sentence using 'As well as'.", spanish: "Significado: Pidieron empanadas así como croquetas.", options: [
      "They ordered empanadas as well as they ordered croquetas.",
      "They ordered empanadas, as well as, croquetas.",
      "They ordered empanadas as well as croquetas.",
      "As well as they ordered empanadas, they ordered croquetas."
  ], correct: 2, explanation: "'As well as' joins two items in a list without needing extra commas or repeating the subject/verb." },
  { type: "usage", emoji: "🤔🌙", english: "Choose the correct sentence using 'Besides'.", spanish: "Significado: Es demasiado tarde para salir; además, está lloviendo.", options: [
      "It's too late to go out besides it's raining.",
      "It's too late to go out; besides, it's raining.",
      "Besides it's too late to go out, it's raining.",
      "It's too late to go out, besides it's raining."
  ], correct: 1, explanation: "'Besides' functioning as an adverb to add a point requires a semicolon or new sentence, followed by a comma." },
  { type: "usage", emoji: "🤔⭐", english: "Choose the correct sentence using 'Moreover'.", spanish: "Significado: El restaurante es famoso. Además, tiene una estrella Michelin.", options: [
      "The restaurant is famous. Moreover, it has a Michelin star.",
      "The restaurant is famous, moreover it has a Michelin star.",
      "Moreover the restaurant is famous it has a Michelin star.",
      "The restaurant is famous moreover, it has a Michelin star."
  ], correct: 0, explanation: "'Moreover' starts a new sentence or follows a semicolon, and is followed by a comma." },
  { type: "usage", emoji: "🤔📈", english: "Choose the correct sentence using 'Furthermore'.", spanish: "Significado: Miami es un centro financiero. Además, es un centro cultural.", options: [
      "Miami is a financial hub, furthermore it is a cultural center.",
      "Miami is a financial hub. Furthermore, it is a cultural center.",
      "Furthermore Miami is a financial hub it is a cultural center.",
      "Miami is a financial hub furthermore, it is a cultural center."
  ], correct: 1, explanation: "'Furthermore' follows the same punctuation rules as 'moreover' and 'however'." },
  { type: "usage", emoji: "🤔🚗", english: "Choose the correct sentence using 'Since'.", spanish: "Significado: Ya que tenemos un auto, podemos conducir hasta Key West.", options: [
      "Since we have a car, we can drive to Key West.",
      "Since, we have a car we can drive to Key West.",
      "We can drive to Key West since, we have a car.",
      "Since of we have a car, we can drive to Key West."
  ], correct: 0, explanation: "When starting a sentence, 'Since' (meaning 'because') introduces a dependent clause, followed by a comma." },
  { type: "usage", emoji: "🤔📋", english: "Choose the correct sentence using 'Unless'.", spanish: "Significado: No puedes entrar al área VIP a menos que estés en la lista.", options: [
      "You can't enter the VIP area, unless, you are on the list.",
      "Unless you aren't on the list, you can't enter the VIP area.",
      "You can't enter the VIP area unless you are on the list.",
      "You can't enter the VIP area unless of you are on the list."
  ], correct: 2, explanation: "'Unless' means 'if not' and directly connects two clauses without extra commas." },
  { type: "usage", emoji: "🤔🌡️", english: "Choose the correct sentence using 'Whereas'.", spanish: "Significado: El invierno aquí es cálido, mientras que el verano es caluroso.", options: [
      "The winter here is warm. Whereas the summer is hot.",
      "The winter here is warm whereas, the summer is hot.",
      "The winter here is warm, whereas the summer is incredibly hot.",
      "Whereas the winter here is warm the summer is incredibly hot."
  ], correct: 2, explanation: "'Whereas' links two contrasting clauses in the same sentence, usually preceded by a comma." },
  { type: "usage", emoji: "🤔🛣️", english: "Choose the correct sentence using 'While'.", spanish: "Significado: Mientras conducía por la I-95, vio un accidente.", options: [
      "While he was driving on I-95, he saw an accident.",
      "While driving on I-95 he saw an accident.",
      "He saw an accident, while he was driving on I-95.",
      "While he was driving on I-95 he saw an accident."
  ], correct: 0, explanation: "When 'While' starts a sentence to show an ongoing action, a comma separates the dependent clause from the main clause." }
];

// --- STYLES INJECTION ---
const injectStyles = () => {
  const style = document.createElement('style');
  style.innerHTML = `
    @import url('https://fonts.googleapis.com/css2?family=Righteous&family=Inter:wght@300;400;600;700&display=swap');
    
    body {
      background: linear-gradient(135deg, #1a0b2e 0%, #0b1a30 100%);
      color: white;
      font-family: 'Inter', sans-serif;
      overflow-x: hidden;
      min-height: 100vh;
    }

    .font-miami {
      font-family: 'Righteous', cursive;
    }

    .neon-text-pink {
      color: #ff2a85;
      text-shadow: 0 0 5px #ff2a85, 0 0 10px #ff2a85, 0 0 20px #ff2a85;
    }
    
    .neon-text-cyan {
      color: #00f3ff;
      text-shadow: 0 0 5px #00f3ff, 0 0 10px #00f3ff, 0 0 20px #00f3ff;
    }

    .glass-card {
      background: rgba(20, 20, 40, 0.7);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(0, 243, 255, 0.2);
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    .btn-option {
      background: transparent;
      border: 2px solid #00f3ff;
      color: #00f3ff;
      transition: all 0.3s ease;
      box-shadow: 0 0 10px rgba(0, 243, 255, 0.1) inset;
    }

    .btn-option:hover:not(:disabled) {
      background: #00f3ff;
      color: #1a0b2e;
      box-shadow: 0 0 15px #00f3ff, 0 0 20px #00f3ff inset;
      transform: translateY(-2px);
    }

    .btn-option.correct {
      background: #00ff88;
      border-color: #00ff88;
      color: #1a0b2e;
      box-shadow: 0 0 15px #00ff88;
    }

    .btn-option.incorrect {
      background: #ff2a85;
      border-color: #ff2a85;
      color: white;
      box-shadow: 0 0 15px #ff2a85;
    }

    .retro-sun {
      position: fixed;
      bottom: -200px;
      left: 50%;
      transform: translateX(-50%);
      width: 600px;
      height: 600px;
      background: linear-gradient(180deg, #ff2a85 0%, #ff8c00 50%, transparent 50%);
      border-radius: 50%;
      z-index: -1;
      opacity: 0.5;
      filter: blur(8px);
      pointer-events: none;
    }
    
    .grid-floor {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 30vh;
      background-image: 
        linear-gradient(rgba(0, 243, 255, 0.2) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0, 243, 255, 0.2) 1px, transparent 1px);
      background-size: 50px 50px;
      transform: perspective(500px) rotateX(60deg);
      z-index: -1;
      pointer-events: none;
    }

    .blank-space {
      display: inline-block;
      min-width: 80px;
      border-bottom: 2px solid #ff2a85;
      text-align: center;
      color: #ff2a85;
      font-weight: bold;
      padding: 0 8px;
    }
    
    .blank-space.correct {
      color: #00ff88;
      border-color: #00ff88;
    }
    
    .blank-space.incorrect {
      color: #ff2a85;
      border-color: #ff2a85;
      text-decoration: line-through;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .animate-fade-in {
      animation: fadeIn 0.4s ease-out forwards;
    }
  `;
  document.head.appendChild(style);
};

const App = () => {
  useEffect(() => {
    injectStyles();
  }, []);

  const [currentQIndex, setCurrentQIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [answered, setAnswered] = useState(false);
  const [selectedIdx, setSelectedIdx] = useState(null);
  const [quizComplete, setQuizComplete] = useState(false);

  const q = quizData[currentQIndex];

  // Auto-advance logic
  useEffect(() => {
    let timer;
    if (answered && !quizComplete) {
      // Auto advance after 4.5 seconds to give time to read explanation,
      // but user can click "Next" button immediately if they want.
      timer = setTimeout(() => {
        handleNext();
      }, 4500);
    }
    return () => clearTimeout(timer);
  }, [answered, currentQIndex, quizComplete]);

  const handleOptionSelect = (idx) => {
    if (answered) return;
    setSelectedIdx(idx);
    setAnswered(true);
    if (idx === q.correct) {
      setScore(prev => prev + 1);
    }
  };

  const handleNext = () => {
    if (currentQIndex < quizData.length - 1) {
      setCurrentQIndex(prev => prev + 1);
      setAnswered(false);
      setSelectedIdx(null);
    } else {
      setQuizComplete(true);
    }
  };

  const restartQuiz = () => {
    setCurrentQIndex(0);
    setScore(0);
    setAnswered(false);
    setSelectedIdx(null);
    setQuizComplete(false);
  };

  // Render question text (handles the fill-in-the-blank logic)
  const renderEnglishSentence = () => {
    if (q.type === 'usage') {
      return <span>{q.english}</span>;
    }
    
    // Fill-in-the-blank
    const parts = q.english.split('_____');
    if (parts.length !== 2) return <span>{q.english}</span>;

    let blankStatusClass = '';
    let blankText = '?';

    if (answered) {
      blankText = q.options[selectedIdx];
      blankStatusClass = selectedIdx === q.correct ? 'correct' : 'incorrect';
    }

    return (
      <span>
        {parts[0]}
        <span className={`blank-space ${blankStatusClass}`}>{blankText}</span>
        {parts[1]}
      </span>
    );
  };

  return (
    <div className="p-4 md:p-8 flex flex-col items-center min-h-screen relative">
      <div className="retro-sun" />
      <div className="grid-floor" />

      <div className="w-full max-w-3xl relative z-10">
        
        {/* Header */}
        <header className="text-center mb-8">
          <h1 className="text-4xl md:text-5xl font-miami neon-text-pink mb-2">Miami Vibes 🌴</h1>
          <h2 className="text-xl md:text-2xl font-miami neon-text-cyan">Linking Words Quiz</h2>
          <div className="mt-4 flex justify-between items-center glass-card rounded-full px-6 py-3">
            <span className="text-sm font-semibold tracking-wider text-gray-300">LEVEL B1</span>
            <span className="text-lg font-bold text-[#00f3ff]">SCORE: {score}/{quizData.length}</span>
          </div>
        </header>

        {/* Quiz Area */}
        {!quizComplete ? (
          <main className="glass-card rounded-3xl p-6 md:p-8 shadow-2xl transition-all duration-300">
            
            {/* Progress */}
            <div className="mb-6">
              <div className="flex justify-between text-xs text-gray-400 mb-2 font-semibold tracking-wider uppercase">
                <span>Question {currentQIndex + 1} of {quizData.length}</span>
              </div>
              <div className="w-full bg-gray-800 rounded-full h-2">
                <div 
                  className="bg-gradient-to-r from-[#00f3ff] to-[#ff2a85] h-2 rounded-full transition-all duration-500 ease-out" 
                  style={{ width: `${((currentQIndex) / quizData.length) * 100}%` }}
                />
              </div>
            </div>

            {/* Question Wrapper with key for animation re-trigger */}
            <div key={currentQIndex} className="animate-fade-in">
              <div className="text-6xl text-center mb-4">{q.emoji}</div>
              
              <div className="mb-8 text-center px-2">
                <p className="text-xl md:text-2xl font-semibold mb-4 leading-relaxed text-white">
                  {renderEnglishSentence()}
                </p>
                <p className="text-md text-gray-400 italic">
                  {q.spanish}
                </p>
              </div>

              {/* Options Grid */}
              <div className={`grid gap-4 mb-6 ${q.type === 'usage' ? 'grid-cols-1' : 'grid-cols-1 md:grid-cols-2'}`}>
                {q.options.map((opt, idx) => {
                  let btnStateClass = '';
                  let disabled = false;
                  
                  if (answered) {
                    disabled = true;
                    if (idx === q.correct) {
                      btnStateClass = 'correct opacity-100 font-bold';
                    } else if (idx === selectedIdx && idx !== q.correct) {
                      btnStateClass = 'incorrect opacity-100 font-bold';
                    } else {
                      btnStateClass = 'opacity-40 border-gray-600 text-gray-400';
                    }
                  }

                  return (
                    <button
                      key={idx}
                      disabled={disabled}
                      onClick={() => handleOptionSelect(idx)}
                      className={`btn-option w-full py-4 px-6 rounded-xl font-medium text-lg leading-snug flex items-center shadow-lg
                        ${q.type === 'usage' ? 'text-left min-h-[4.5rem]' : 'text-center justify-center'} 
                        ${btnStateClass}
                      `}
                    >
                      {opt}
                    </button>
                  );
                })}
              </div>

              {/* Feedback Box */}
              {answered && (
                <div className="mt-6 bg-black/40 border border-[#00f3ff]/30 p-5 rounded-2xl animate-fade-in flex flex-col items-center text-center">
                  <div className="text-2xl font-bold mb-2">
                    {selectedIdx === q.correct ? (
                      <span className="text-[#00ff88]">¡Correcto! 😎</span>
                    ) : (
                      <span className="text-[#ff2a85]">Incorrecto 🚫</span>
                    )}
                  </div>
                  <p className="text-gray-200 text-md leading-relaxed mb-5 max-w-xl">
                    {q.explanation}
                  </p>
                  
                  <button 
                    onClick={handleNext}
                    className="bg-gradient-to-r from-[#ff2a85] to-[#ff6a00] hover:from-[#ff6a00] hover:to-[#ff2a85] text-white font-bold py-3 px-10 rounded-full transition-all duration-300 transform hover:scale-105 shadow-[0_0_15px_rgba(255,42,133,0.5)] flex items-center gap-2"
                  >
                    <span>Next Question</span>
                    <span>➡️</span>
                  </button>
                </div>
              )}
            </div>

          </main>
        ) : (
          /* End Screen */
          <div className="glass-card rounded-3xl p-10 text-center animate-fade-in shadow-[0_0_40px_rgba(255,42,133,0.3)] border border-[#ff2a85]">
            <div className="text-7xl mb-6">🏆🍹</div>
            <h2 className="text-5xl font-miami neon-text-pink mb-4">Quiz Complete!</h2>
            <p className="text-2xl text-gray-200 mb-8">
              Final Score: <span className="font-bold text-4xl neon-text-cyan block mt-3">{score} / {quizData.length}</span>
            </p>
            
            <div className="mb-10 text-lg text-gray-300">
              {score === quizData.length && "Perfect! You're the absolute boss of Miami! 🏝️"}
              {score >= quizData.length * 0.8 && score < quizData.length && "Great job! Your English is heating up like Miami summer! ☀️🕶️"}
              {score >= quizData.length * 0.5 && score < quizData.length * 0.8 && "Not bad! Keep practicing those linking words to ride the wave! 🌴📚"}
              {score < quizData.length * 0.5 && "Don't worry! Review the rules and try again. You'll get it next time! 🌊🏄‍♂️"}
            </div>

            <button 
              onClick={restartQuiz} 
              className="bg-[#00f3ff] hover:bg-white text-[#1a0b2e] font-bold py-4 px-12 rounded-full text-xl transition-all duration-300 transform hover:scale-105 shadow-[0_0_20px_rgba(0,243,255,0.6)]"
            >
              Play Again 🔁
            </button>
          </div>
        )}

      </div>
    </div>
  );
};

export default App;