# Test API endpoints using curl

# Set CODESPACE_NAME variable (replace with your actual codespace name if running manually)
CODESPACE_NAME=${CODESPACE_NAME}
BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"

# Test API root
curl -k "$BASE_URL/"

# Test activities endpoint
curl -k "$BASE_URL/api/activities/"

# Test users endpoint
curl -k "$BASE_URL/api/users/"

# Test teams endpoint
curl -k "$BASE_URL/api/teams/"

# Test workouts endpoint
curl -k "$BASE_URL/api/workouts/"

# Test leaderboard endpoint
curl -k "$BASE_URL/api/leaderboard/"

# For localhost testing
curl -k "http://localhost:8000/api/activities/"
