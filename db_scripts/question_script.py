from app.extensions import db
from app.models.question import Question

db.create_all()

q1 = Question(content="Why is the sky blue?", answer="Because... Why not?")
q2 = Question(content="What is love?", answer="A portal to the underworld.")
db.session.add_all([q1, q2])
db.session.commit()
