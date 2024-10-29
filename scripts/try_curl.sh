rm test/test_data/in.margins.pdf 2>/dev/null | true

curl -X POST "http://127.0.0.1:8000/add_margins/" \
  -F "file=@test/test_data/in.pdf" \
  -F "left=150" \
  -F "right=150" \
  -F "top=0" \
  -F "bottom=0" \
  -F "force_relative=false" \
  --output test/test_data/in.margins.pdf

echo "output written to test/test_data/in.margins.pdf"
