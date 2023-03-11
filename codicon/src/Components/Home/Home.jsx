import React from 'react'
import './Home.css'
import question from '../../assets/question.png'
import auction from '../../assets/auction.png'
import deal from '../../assets/deal.png'

function Home() {
  
    return (
    <div className='home'>
      <h1 className='gradient__text'>Bienvenidos a Subastas de Cajas Misteriosas</h1>
      <div className='home-container'>
        <div className='home-container-item'>
          <img src={question} alt='Imagen de una caja misteriosa' />
          <p className='home-container-item-title'>¿Qué es una caja misteriosa?</p>
          <p className='home-container-item-text'>
            Una caja misteriosa es un paquete que contiene artículos sorpresa de diferentes categorías.
            ¡Nunca sabes lo que puedes encontrar dentro de una caja misteriosa!
          </p>
        </div>
        <div className='home-container-item'>
          <img src={auction} alt='Imagen de una subasta' />
          <p className='home-container-item-title'>¿Cómo funciona una subasta?</p>
          <p className='home-container-item-text'>
            Las subastas son eventos en los que los usuarios pueden hacer ofertas en tiempo real
            para ganar la posesión de una caja misteriosa.
          </p>
        </div>
        <div className='home-container-item'>
          <img src={deal} alt='Imagen de una caja misteriosa' />
          <p className='home-container-item-title'>¿Por qué debería participar en una subasta?</p>
          <p className='home-container-item-text'>
            Participar en una subasta es emocionante y te brinda la oportunidad de obtener una caja misteriosa única
            que podría contener artículos que de otra manera no tendrías acceso.
          </p>
        </div>
      </div>
    </div>
  )
}

export default Home
