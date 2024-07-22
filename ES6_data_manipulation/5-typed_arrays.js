export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8Array = new DataView(buffer);

  if (position >= length) {
    throw new Error('Position outside range');
  }

  int8Array.setInt8(position, value);
  return int8Array;
}
  