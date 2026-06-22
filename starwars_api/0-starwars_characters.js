#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

async function getCharacters () {
  try {
    const filmData = await makeRequest(url);
    const charactersUrls = filmData.characters;

    if (!charactersUrls) {
      console.error(`FilmsID ${movieId}, not found.`);
      return;
    }

    for (const characterUrl of charactersUrls) {
      const characterData = await makeRequest(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

getCharacters();
