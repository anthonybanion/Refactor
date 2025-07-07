<?php

namespace App\Controller;

use App\Entity\Personal;
use App\Form\PersonalType;
use App\Repository\PersonalRepository;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

use Symfony\Component\HttpFoundation\File\Exception\FileException;
use Symfony\Component\String\Slugger\SluggerInterface;

#[Route('/personal')]
class PersonalController extends AbstractController
{
    #[Route('/', name: 'app_personal_index', methods: ['GET'])]
    public function index(PersonalRepository $personalRepository): Response
    {
        return $this->render('personal/index.html.twig', [
            'personals' => $personalRepository->findAll(),
        ]);
    }

    #[Route('/new', name: 'app_personal_new', methods: ['GET', 'POST'])]
    public function new(Request $request, EntityManagerInterface $entityManager): Response
    {
        $personal = new Personal();
        $form = $this->createForm(PersonalType::class, $personal);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $entityManager->persist($personal);
            $entityManager->flush(); // Genera el ID

            $fotoFile = $form->get('foto')->getData();
            if ($fotoFile) {
                $nombreArchivo = $personal->getId() . '.' . $fotoFile->guessExtension();
                try {
                    $fotoFile->move(
                        $this->getParameter('fotos_personal_dir'),
                        $nombreArchivo
                    );
                } catch (FileException $e) {
                    //  manejar error
                }
            }

            return $this->redirectToRoute('app_personal_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('personal/new.html.twig', [
            'personal' => $personal,
            'form' => $form,
        ]);
    }


    #[Route('/{id}', name: 'app_personal_show', methods: ['GET'])]
    public function show(Personal $personal): Response
    {
        return $this->render('personal/show.html.twig', [
            'personal' => $personal,
        ]);
    }

    #[Route('/{id}/edit', name: 'app_personal_edit', methods: ['GET', 'POST'])]
    public function edit(Request $request, Personal $personal, EntityManagerInterface $entityManager): Response
    {
        $form = $this->createForm(PersonalType::class, $personal);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $fotoFile = $form->get('foto')->getData();
            if ($fotoFile) {
                $nombreArchivo = $personal->getId() . '.' . $fotoFile->guessExtension();
                try {
                    $fotoFile->move(
                        $this->getParameter('fotos_personal_dir'),
                        $nombreArchivo
                    );
                } catch (FileException $e) {
                    // Opcional: manejar error
                }
            }

            $entityManager->flush();

            return $this->redirectToRoute('app_personal_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('personal/edit.html.twig', [
            'personal' => $personal,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_personal_delete', methods: ['POST'])]
    public function delete(Request $request, Personal $personal, EntityManagerInterface $entityManager): Response
    {
        if ($this->isCsrfTokenValid('delete'.$personal->getId(), $request->request->get('_token'))) {
            $entityManager->remove($personal);
            $entityManager->flush();
        }

        return $this->redirectToRoute('app_personal_index', [], Response::HTTP_SEE_OTHER);
    }
}
