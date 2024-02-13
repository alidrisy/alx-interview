#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function charRequest (characters, num) {
  if (num >= characters.length) return;

  request.get(characters[num], (_req, resp) => {
    const charBody = JSON.parse(resp.body);
    const charName = charBody.name;
    console.log(charName);
    charRequest(characters, num + 1);
  });
}

request.get(url, (_req, resp) => {
  if (resp) {
    const body = JSON.parse(resp.body);
    const characters = body.characters;
    charRequest(characters, 0);
  }
});
