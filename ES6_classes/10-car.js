export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  cloneCar() {
    const clone = Object.create(Object.getPrototypeOf(this));
    const sym = Symbol();
    for (const key of Object.getOwnPropertyNames(this)) {
      clone[key] = this[key];
    }
    return clone;
  }
}
